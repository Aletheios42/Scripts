#include <stdio.h>
#include <stdlib.h>

#define CLIPBOARD_CMD "xclip -selection clipboard -o"

int main() {
  FILE *fp;
  char buffer[1024];

  // Ejecutar el comando xclip para obtener el contenido del portapapeles
  fp = popen(CLIPBOARD_CMD, "r");
  if (fp == NULL) {
    perror("popen");
    return EXIT_FAILURE;
  }

  // Leer el contenido del portapapeles
  while (fgets(buffer, sizeof(buffer), fp) != NULL) {
    printf("%s", buffer);
  }

  // Cerrar el pipe
  pclose(fp);

  return EXIT_SUCCESS;
}
