#ifndef SLIDE_LINE_H
#define SLIDE_LINE_H

#include <stdlib.h>
#include <stdio.h>
#include <stddef.h>

#define SLIDE_LEFT 0
#define SLIDE_RIGHT 1
#define LINE_SIZE 2048

int slide_line(int *line, size_t size, int direction);

#endif /* SLIDE_LINE_H */

