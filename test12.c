#include <stdio.h>
#include <math.h>

int main()
{
    double x,a,g;
    scanf("%lf",&a);
    scanf("%lf",&x);
    g = sin(a*x)*cos(a-x);
    printf("g = %f",g);
    return 0;
}