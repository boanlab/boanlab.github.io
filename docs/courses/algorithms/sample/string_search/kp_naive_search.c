# include <stdio.h>
# include <string.h>
#define _CRT_SECURE_NO_WARNINGS

void naivePatternSearch (char T[], char P[]) {

  int n = strlen(T);
  int m = strlen(P);

  for (int i = 0; i <= n-m; i++) {

    for (int j = 0; j < m; j++) { 

      if (T[i+j] != P[j])
        break;

      if (j == m-1) {

        printf("Pattern found at index %d \n", i);
        break;

      }
    }
  }
}

int main() {

    char text[] = "ABAAA";
    char pattern[] = "AA";


    naivePatternSearch(text,pattern);
}