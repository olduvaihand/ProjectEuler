﻿/*
 * ProjectEuler/src/c/Problem256.c
 *
 * Tatami-Free Rooms
 * =================
 * Published on Saturday, 19th September 2009, 01:00 am
 *
 * Tatami are rectangular mats, used to completely cover the floor of a room,
 * without overlap. Assuming that the only type of available tatami has
 * dimensions 12, there are obviously some limitations for the shape and size of
 * the rooms that can be covered. For this problem, we consider only rectangular
 * rooms with integer dimensions a, b and even size s = a·b.  We use the term
 * 'size' to denote the floor surface area of the room, and — without loss of
 * generality — we add the condition a  b. There is one rule to follow when
 * laying out tatami: there must be no points where corners of four different
 * mats meet.  For example, consider the two arrangements below for a 44 room:
 * The arrangement on the left is acceptable, whereas the one on the right is
 * not: a red "X" in the middle, marks the point where four tatami meet. Because
 * of this rule, certain even-sized rooms cannot be covered with tatami: we call
 * them tatami-free rooms.  Further, we define T(s) as the number of tatami-free
 * rooms of size s. The smallest tatami-free room has size s = 70 and dimensions
 * 710.  All the other rooms of size s = 70 can be covered with tatami; they
 * are: 170, 235 and 514.  Hence, T(70) = 1. Similarly, we can verify that
 * T(1320) = 5 because there are exactly 5 tatami-free rooms of size s = 1320:
 * 2066, 2260, 2455, 3044 and 3340.  In fact, s = 1320 is the smallest room-size
 * s for which T(s) = 5. Find the smallest room-size s for which T(s) = 200.
 */
 
#include <stdio.h>
#include "ProjectEuler/ProjectEuler.h"
#include "ProjectEuler/Problem256.h"


int main(int argc, char** argv) {

    return 0;
}