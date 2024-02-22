#include <stdio.h>

typedef float (*t_function)(float x);

typedef struct s_inner_data {
	float		x;
	t_function	function;
}	t_inner_data;

typedef float (*t_inner_func)(t_inner_data *data);

typedef struct s_inner {
	t_inner_func	func;
	t_inner_data	data;
}	t_inner;

float inner(t_inner_data *data)
{
    data->x = data->function(data->x);
    return data->x;
}

t_inner	outer(float x, t_function function)
{
	return ((t_inner){inner, {x, function}});
}

float square(float x)
{
	return (x * x);
}

int main(void)
{
	t_inner my_counter = outer(3, square);

    float a = my_counter.func(&my_counter.data);
    float b = my_counter.func(&my_counter.data);

	printf("%f\n", a);
	printf("%f\n", b);
	printf("%f\n", my_counter.func(&my_counter.data));

	t_inner another_counter = outer(2, square);

	printf("%f\n", another_counter.func(&another_counter.data));
	printf("%f\n", another_counter.func(&another_counter.data));
	printf("%f\n", another_counter.func(&another_counter.data));
}
