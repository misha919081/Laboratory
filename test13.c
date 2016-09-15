#include <stdio.h>
#include <math.h>

int main()
{
    int x;
    double g;
    scanf("%d",&x);
    g = log((float)x)/log(2.0);
    printf("g = %lf",g);

    return 0;
}