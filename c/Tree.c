#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

void print_tree(const char *basepath, int depth) {
  struct dirent *dp;
  DIR *dir = opendir(basepath);

  if (!dir) {
    perror("opendir");
    return;
  }

  while ((dp = readdir(dir)) != NULL) {
    // Skip "." and ".."
    if (dp->d_name[0] == '.')
      continue;

    // Print the current file/directory
    for (int i = 0; i < depth; i++)
      printf("    ");
    printf("%s\n", dp->d_name);

    // If it's a directory, recursively print its contents
    if (dp->d_type == DT_DIR) {
      char path[1024];
      snprintf(path, sizeof(path), "%s/%s", basepath, dp->d_name);
      print_tree(path, depth + 1);
    }
  }

  closedir(dir);
}

int main(int argc, char *argv[]) {
  if (argc < 2) {
    fprintf(stderr, "Usage: %s <directory>\n", argv[0]);
    return EXIT_FAILURE;
  }

  print_tree(argv[1], 0);
  return EXIT_SUCCESS;
}

