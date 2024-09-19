#include <errno.h>
#include <fcntl.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#define BATTERY_FILE "/sys/class/power_supply/BAT0/capacity"
#define NOTIFY_COMMAND "notify-send"

// Umbrales de batería para notificación
int battery_levels[] = {20, 15, 10, 8, 6, 5, 4};
int notified_levels[] = {0, 0, 0, 0, 0, 0, 0};

void daemonize();
void battery_notify();
int get_battery_level();

void daemonize() {
  // Establecer el entorno DISPLAY para el comando notify-send
  setenv("DISPLAY", ":0", 1);

  // Daemon en ejecución
  while (1) {
    battery_notify(); // Llamada para verificar el nivel de batería y enviar
                      // notificaciones
    sleep(60);        // Espera de 60 segundos
  }
}

void battery_notify() {
  int level = get_battery_level();
  if (level == -1) {
    return; // No se pudo obtener el nivel de batería
  }

  // Agregar mensaje de depuración
  printf("Battery level: %d%%\n", level);

  for (int i = 0; i < sizeof(battery_levels) / sizeof(battery_levels[0]); ++i) {
    if (level <= battery_levels[i] && !notified_levels[i]) {
      char command[256];
      snprintf(command, sizeof(command), "%s \"Battery level at %d%%\"",
               NOTIFY_COMMAND, battery_levels[i]);
      int ret = system(command);
      if (ret != 0) {
        printf("Error executing notify-send command, return code: %d\n", ret);
      }

      printf("Sent notification for %d%%\n", battery_levels[i]);

      notified_levels[i] = 1; // Marcar el nivel como notificado
    }
  }

  // Restablecer niveles notificados si la batería sube por encima del umbral
  for (int i = 0; i < sizeof(battery_levels) / sizeof(battery_levels[0]); ++i) {
    if (level > battery_levels[i]) {
      notified_levels[i] = 0;
    }
  }
}

int get_battery_level() {
  FILE *file = fopen(BATTERY_FILE, "r");
  if (!file) {
    perror("fopen");
    return -1;
  }

  int level;
  if (fscanf(file, "%d", &level) != 1) {
    perror("fscanf");
    fclose(file);
    return -1;
  }

  fclose(file);
  return level;
}

int main() {
  daemonize();
  return 0;
}
