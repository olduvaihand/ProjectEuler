﻿/*
 * ProjectEuler/src/c/Problem186.c
 *
 * Connectedness of a network.
 * ===========================
 * Published on Saturday, 15th March 2008, 05:00 am
 *
 * Here are the records from a busy telephone system with one million users:
 * RecNrCallerCalled 1200007100053 2600183500439 3600863701497 .........   The
 * telephone number of the caller and the called number in record n are
 * Caller(n) = S2n-1 and Called(n) = S2n where S1,2,3,... come from the "Lagged
 * Fibonacci Generator": For 1  k  55, Sk = [100003 - 200003k + 300007k3]
 * (modulo 1000000)  For 56  k, Sk = [Sk-24 + Sk-55] (modulo 1000000) If
 * Caller(n) = Called(n) then the user is assumed to have misdialled and the
 * call fails; otherwise the call is successful. From the start of the records,
 * we say that any pair of users X and Y are friends if X calls Y or vice-versa.
 * Similarly, X is a friend of a friend of Z if X is a friend of Y and Y is a
 * friend of Z; and so on for longer chains. The Prime Minister's phone number
 * is 524287. After how many successful calls, not counting misdials, will 99%
 * of the users (including the PM) be a friend, or a friend of a friend etc., of
 * the Prime Minister?
 */
 
#include <stdio.h>
#include "ProjectEuler/ProjectEuler.h"
#include "ProjectEuler/Problem186.h"


int main(int argc, char** argv) {

    return 0;
}