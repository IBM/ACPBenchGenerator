
/*
 * frog_problem_gen.c
 * PDDL problem generator for the "frog-jumping" domain.
 *
 * Layout:
 *   Pads p1..pK left-to-right, where K = L + R + 1.
 *   Initial:  l1..lL at p1..pL, empty at p(L+1), r1..rR at p(L+1+1)..pK.
 *   Goal:     r1..rR at p1..pR, empty at p(R+1),  l1..lL at p(R+1+1)..pK.
 *
 * Domain assumptions (as in the corrected domain above):
 *   - Types: leftfrog, rightfrog, lilypad; actions use only (at/empty/next).
 *
 * Build: cc -O2 -Wall -ansi -o frog_problem_gen frog_problem_gen.c
 * Usage:
 *   ./frog_problem_gen -n 3 [-domain frog-jumping] [-problem frogs-3v3]
 *   ./frog_problem_gen -L 2 -R 3 > frogs-2v3.pddl
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* -------- Globals -------- */
static int  gL = -1;                  /* # left frogs  */
static int  gR = -1;                  /* # right frogs */
static char gDomain[128]  = "frogs-jumping";
static char gProblem[128] = "";       /* default set later */

/* -------- Usage -------- */
static void usage(const char *prog) {
  fprintf(stderr, "Usage: %s [-n N | -L L -R R] [-domain NAME] [-problem NAME]\n", prog);
  fprintf(stderr, "  -n N           symmetric puzzle: N left + N right frogs (>=1)\n");
  fprintf(stderr, "  -L L -R R      asymmetric: L left frogs, R right frogs (each >=1)\n");
  fprintf(stderr, "  -domain NAME   PDDL domain name (default: frog-jumping)\n");
  fprintf(stderr, "  -problem NAME  problem name (default: frogs-<L>v<R>)\n");
}

/* -------- Argument parsing (ANSI/C89) -------- */
static int parse_args(int argc, char **argv) {
  int i = 1;
  if (argc == 1) return 0;

  while (i < argc) {
    if (strcmp(argv[i], "-n") == 0) {
      if (i + 1 >= argc) return 0;
      gL = gR = atoi(argv[i + 1]);
      i += 2;
    } else if (strcmp(argv[i], "-L") == 0) {
      if (i + 1 >= argc) return 0;
      gL = atoi(argv[i + 1]);
      i += 2;
    } else if (strcmp(argv[i], "-R") == 0) {
      if (i + 1 >= argc) return 0;
      gR = atoi(argv[i + 1]);
      i += 2;
    } else if (strcmp(argv[i], "-domain") == 0) {
      if (i + 1 >= argc) return 0;
      strncpy(gDomain, argv[i + 1], sizeof(gDomain) - 1);
      gDomain[sizeof(gDomain) - 1] = '\0';
      i += 2;
    } else if (strcmp(argv[i], "-problem") == 0) {
      if (i + 1 >= argc) return 0;
      strncpy(gProblem, argv[i + 1], sizeof(gProblem) - 1);
      gProblem[sizeof(gProblem) - 1] = '\0';
      i += 2;
    } else {
      return 0; /* unknown flag */
    }
  }

  if (gL < 1 && gR < 1) return 0;
  if (gL < 1 && gR >= 1) return 0;
  if (gR < 1 && gL >= 1) return 0;

  if (gProblem[0] == '\0') {
    sprintf(gProblem, "frogs-%dv%d", gL, gR);
  }
  return 1;
}

int main(int argc, char **argv) {
  int i;
  int pads;

  if (!parse_args(argc, argv)) {
    usage(argv[0]);
    return 1;
  }

  pads = gL + gR + 1; /* total pads */

  /* ---------- Header ---------- */
  printf("(define (problem %s)\n", gProblem);
  printf("  (:domain %s)\n", gDomain);

  /* ---------- Objects ---------- */
  printf("  (:objects\n    ");
  /* left frogs */
  for (i = 1; i <= gL; ++i) printf("l%d ", i);
  printf("- leftfrog\n    ");
  /* right frogs */
  for (i = 1; i <= gR; ++i) printf("r%d ", i);
  printf("- rightfrog\n    ");
  /* pads */
  for (i = 1; i <= pads; ++i) printf("p%d ", i);
  printf("- lilypad)\n");

  /* ---------- Init ---------- */
  printf("  (:init\n");

  /* chain adjacency: (next p1 p2) ... (next p{K-1} pK) */
  for (i = 1; i <= pads - 1; ++i) {
    printf("    (next p%d p%d)\n", i, i + 1);
  }

  /* left frogs at p1..pL */
  for (i = 1; i <= gL; ++i) {
    printf("    (at l%d p%d)\n", i, i);
  }

  /* empty at p(L+1) */
  printf("    (empty p%d)\n", gL + 1);

  /* right frogs at p(L+1+1) .. p(L+1+R) == p(L+R+1) */
  for (i = 1; i <= gR; ++i) {
    printf("    (at r%d p%d)\n", i, gL + 1 + i);
  }

  printf("  )\n");

  /* ---------- Goal ---------- */
  printf("  (:goal (and\n");

  /* right frogs must occupy left segment p1..pR */
  for (i = 1; i <= gR; ++i) {
    printf("    (at r%d p%d)\n", i, i);
  }

  /* empty must be between groups after swap:
     at p(R+1). For symmetric L=R this equals initial empty cell. */
  printf("    (empty p%d)\n", gR + 1);

  /* left frogs must occupy right segment p(R+1+1)..p(R+1+L) */
  for (i = 1; i <= gL; ++i) {
    printf("    (at l%d p%d)\n", i, gR + 1 + i);
  }

  printf("  ))\n");
  printf(")\n");

  return 0;
}
