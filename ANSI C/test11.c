#include <stdio.h>

int main()
{
    float x,a,q;
    scanf("%f",&a);
    scanf("%f",&x);
    q = a+x; printf("q1 = %f\n",q);
    q = a+x*a; printf("q2 = %f\n",q);
    q = (a+x)*a; printf("q3 = %f\n",q);
    q = (a+x)/3.5f; printf("q4 = %f\n",q);
    q = (a+x)/(2+a); printf("q5 = %f\n",q);
    q /= 10; printf("q6 = %f\n",q);
    return 0;
}