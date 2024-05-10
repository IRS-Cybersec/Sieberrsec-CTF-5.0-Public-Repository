#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void setup() {
  setbuf(stdin, 0);
  setbuf(stdout, 0);
  setbuf(stderr, 0);
}

void *chunks[0x3];
void *last_chunk;

void menu() {
  puts("1. Create");
  puts("2. Read");
  puts("3. Update");
  puts("4. Delete");
  puts("5. Exit");
}

void c() {
  int idx = 0;
  char buf[0x100];

  puts("Index: ");
  fgets(buf, 0x10 - 1, stdin);
  idx = atoi(buf);
  if (idx < 0 || idx >= 0x3) {
    puts("Invalid index");
    return;
  }

  chunks[idx] = malloc(0x1008);
  if (chunks[idx] == NULL) {
    puts("Malloc error");
    return;
  }

  puts("Data: ");
  read(0, chunks[idx], 0x1008);
  last_chunk = chunks[idx];
}

void r() {
  int idx = 0;
  char buf[0x100];

  puts("Index: ");
  fgets(buf, 0x10 - 1, stdin);
  idx = atoi(buf);
  if (idx < 0 || idx >= 0x3) {
    puts("Invalid index");
    return;
  }

  if (chunks[idx] == NULL) {
    puts("Invalid chunk");
    return;
  }

  printf("Content: %s\n", chunks[idx]);
  last_chunk = chunks[idx];
}

void u() {
  int idx = 0;
  char buf[0x100];

  puts("Index: ");
  fgets(buf, 0x10 - 1, stdin);
  idx = atoi(buf);
  if (idx < 0 || idx >= 0x3) {
    puts("Invalid index");
    return;
  }

  if (chunks[idx] == NULL) {
    puts("Invalid chunk");
    return;
  }

  puts("Data: ");
  read(0, chunks[idx], 0x1008);
  last_chunk = chunks[idx];
}

void d() {
  int idx = 0;
  char buf[0x100];

  puts("Index: ");
  fgets(buf, 0x10 - 1, stdin);
  idx = atoi(buf);
  if (idx < 0 || idx >= 0x3) {
    puts("Invalid index");
    return;
  }

  if (chunks[idx] == NULL) {
    puts("Invalid chunk");
    return;
  }

  free(chunks[idx]);
  last_chunk = chunks[idx];
}

int main() {
  char buf[0x100];
  int choice;
  int view_chance = 1;

  setup();

  while (1) {
    menu();
    fgets(buf, 0x10 - 1, stdin);
    choice = atoi(buf);

    switch (choice) {
      case 1:
        c();
        break;
      case 2:
        if (view_chance) {
          view_chance = 0;
          r();
        } else {
          puts("No more leaks");
        }
        break;
      case 3:
        u();
        break;
      case 4:
        d();
        break;
      case 5:
        puts("Bye");
        return 0;
      default:
        puts("Invalid choice");
        break;
    }
  }
}
