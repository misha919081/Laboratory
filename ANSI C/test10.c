#include <stdio.h>

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