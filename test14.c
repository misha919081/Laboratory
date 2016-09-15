#include <stdio.h>
#include <math.h>

int main() {
    float a,x;
    double G,F,Y;
    scanf("%f",&a);
    scanf("%f",&x);
    G = ((2*(-5*a*a+3*a*x+2*x*x))/(5*a*a+9*a*x-2*x*x))*-1;
    F = sin(3.14*(10*a*a+37*a*x+7*x*x))/(3.14*(10*a*a+37*a*x+7*x*x));
    Y = log(-5*a*a-16*a*x+16*x*x+1)/log(2.0);
    printf("G = %f\n",G);
    printf("F = %f\n",F);
    printf("Y = %f\n",Y);
    return 0;
}