main()  # test1
{

}

int main()  # test2
{
    return 0;
}

#include <stdio.h>  # test3

int main() {
    printf("Hello, world!\n");
    return 0;
}

#include <stdio.h>  # test4

int main() {

    printf("%d\n",10);
    printf("%5d\n",10);
    printf("%05d\n",10);

    printf("\n");

    printf("%i\n",10);
    printf("%5i\n",10);
    printf("%05i\n",10);
    return 0;
}

#include <stdio.h>  # test5

int main() {

    printf("%f\n", 0.545435433453454 );

    printf("%2.1f\n", 10.545435433453454 );
    printf("%2.2f\n", 10.545435433453454 );
    printf("%2.3f\n", 10.545435433453454 );

    printf("%2.4f\n", 0.545435433453454 );
    printf("%.4f\n", 0.545435433453454 );
    return 0;
}

#include <stdio.h>  # test6

int main() {
    printf("%c\n",'H' );
    printf("%c\n",'e' );
    printf("%c\n",'l' );
    printf("%c\n",'l' );
    printf("%c\n",'o' );
    printf("%c%c%c%c%c\n",'H','e','l','l','o' );
    printf("%s\n","Hello, world!" );
    return 0;
}

#include <stdio.h>  # test7

int main() {

    printf("Decimal: %d\n", 255);
    printf("Hexadecimal: %x\n", 255);
    printf("Hexadecimal: %X\n", 255);
    printf("Octal: %o\n", 255);
    return 0;
}

#include <stdio.h>  # test8

int main() {

    int IDEAL_METRIC_METER = 1;
    float PI = 3.14;
    char CHAR = 'A';

    printf("%d\n", IDEAL_METRIC_METER);
    printf("%f\n", PI);
    printf("%c\n\n",CHAR);

    IDEAL_METRIC_METER = 2;
    PI = 3.15;
    CHAR = 'B';

    printf("%d\n", IDEAL_METRIC_METER);
    printf("%f\n", PI);
    printf("%c\n",CHAR);
    return 0;
}

#include <stdio.h>  # test9

int main()
{

    const int IDEAL_METRIC_METER = 1;
    const float PI = 3.14;
    const char CHAR = 'A';

    printf("%d\n", IDEAL_METRIC_METER);
    printf("%f\n", PI);
    printf("%c\n", CHAR);

    return 0;
}

#include <stdio.h>  # test10

int main()
{
    int IDEAL_METRIC_METER;
    float car_length;
    char _char;

    scanf("%d %f %c", &IDEAL_METRIC_METER, &car_length, &_char);
    getchar();
    printf("%d\n", IDEAL_METRIC_METER);
    printf("%f\n", car_length);
    printf("%c\n\n", _char);
    return 0;
}

#include <stdio.h> # test11

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

#include <stdio.h>  # test12
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

#include <stdio.h>  # test13
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

#include <stdio.h>  # test14
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
