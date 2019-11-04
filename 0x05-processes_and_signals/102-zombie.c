#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"
/**
 * infinite_while - description
 * Return: int
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - main function
 * Return: int
*/
int main(void)
{
	int zombie, i;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (zombie == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", getpid());
	}
	return (infinite_while());
}
