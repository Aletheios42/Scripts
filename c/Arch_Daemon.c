#include <errno.h>
#include <fcntl.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

void battery_notify();
void clipboard_notify();

void daemonize() {
  pid_t pid;

  // Fork para crear un proceso hijo
  pid = fork();
  if (pid < 0) {
    exit(EXIT_FAILURE);
  }
  if (pid > 0) {
    // Salir del proceso padre
    exit(EXIT_SUCCESS);
  }

  // Crear una nueva sesión y hacer que el proceso sea el líder
  if (setsid() < 0) {
    exit(EXIT_FAILURE);
  }

  // Manejar señales
  signal(SIGHUP, SIG_IGN);

  // Hacer otro fork para asegurar que el daemon no pueda adquirir un terminal
  pid = fork();
  if (pid < 0) {
    exit(EXIT_FAILURE);
  }
  if (pid > 0) {
    // Salir del proceso padre
    exit(EXIT_SUCCESS);
  }

  // Cambiar el directorio de trabajo al directorio raíz
  if (chdir("/") < 0) {
    exit(EXIT_FAILURE);
  }

  // Cerrar los descriptores de archivo estándar
  close(STDIN_FILENO);
  close(STDOUT_FILENO);
  close(STDERR_FILENO);

  // Opcional: Redirigir la salida a un archivo de log
  open("/var/log/daemon.log", O_WRONLY | O_CREAT | O_APPEND, 0640);
  dup2(STDOUT_FILENO, STDERR_FILENO);

  // Daemon en ejecución
  while (1) {
    // Aquí es donde el daemon realiza su trabajo
    sleep(60); // Espera de 60 segundos
  }
}

int main() {
  daemonize();
  return 0;
}
