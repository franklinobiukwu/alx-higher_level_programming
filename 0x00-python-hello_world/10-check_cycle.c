#include "lists.h"
#define SIZE 1000

/**
* check_cycle - checks if a singly linked list has a cycle in it
*
* @list: head pointer of singly linked list
*
* Return: 0 if there is no cycle or
* 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *address_array[SIZE];
	int found = 0;
	int count = -1;
	int i;


	while (current)
	{
		/*
		 * check if current has been visited previously.
		 * Set found to 1 and exit loop if previously visited
		 */
		for (i = 0; i <= count; i++)
		{
			if (address_array[i] == current)
			{
				found = 1;
				break;
			}
		}
		if (found == 1)
			break;

		/* store current address in array if not previously visited */
		count++;
		address_array[count] = current;
		/* advance to next node */
		current = current->next;
	}

	return (found);
}
