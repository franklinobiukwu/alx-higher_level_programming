#include "lists.h"

#define RANGE 1000

/**
* is_palindrome - Function that checks if a singly linked list is a palindrome
*
* @head: pointer to head pointer of list
*
* Return: 0 if not a palindrome or 1 if it is a palindrome
*/


int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int i = 0;
	int arr[RANGE];

	while (current)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	current = *head;
	while (current)
	{
		if (arr[i - 1] != current->n)
			return (0);
		i--;
	}
	return (1);
}
