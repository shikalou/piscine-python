#include <stdio.h>

typedef	int (*t_add_n)(int);

t_add_n	add(int a)
{
	int add_n(int b)
	{
		return (a + b);
	}
	return (add_n);
}

int main(void)
{
	t_add_n	first = add(0);
	
	printf("%d\n", first(42));
}
