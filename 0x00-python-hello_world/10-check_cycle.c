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
	listint_t *slow = list;
	listint_t *fast = list;
	int found = 0;


	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			found = 1;
			break;
		}
	}

	return (found);
}
