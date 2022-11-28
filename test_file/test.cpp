#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>

using namespace std;

int n, S[10000];

void print_array()
{
    for(int i = 0; i < n; i++)
    {
        printf("%d", S[i]);
    }
    printf("\n");
}

void swap(int a, int b)
{
    int t = S[a];
    S[a] = S[b];
    S[b] = t;
}

void selection_sort(void)
{
    for(int i; i < n-1; i++)
    {
        for(int j = j + 1; j < n; j++)
        {
            if(S[i] > S[j])
            {
                swap(i, j);
            }
        }
    }
}

int main()
{
    printf("test\n");
    srand(time(NULL));
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
    {
        S[i] = rand();
    }
    int start = clock();

    selection_sort();
    printf("Result = %.31f(sec)\n", (double)(clock()-start)/CLOCKS_PER_SEC);
    //printf(std::sort(S, S+n));
    return 0;
}