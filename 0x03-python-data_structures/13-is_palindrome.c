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
	listint_t *current;
	listint_t *next, *prev = NULL;
	listint_t *slow = *head, *fast = *head;


	/* Treaverse to the middle of list */
	while (fast)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	/* Reverse the list from the middle */
	current = slow;
	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	/* Compare both list */
	while (prev)
	{
		if ((*head)->n == prev->n)
		{
			*head = (*head)->next;
			prev = prev->next;
		}
		else
			return (0);
	}
	return (1);
}
