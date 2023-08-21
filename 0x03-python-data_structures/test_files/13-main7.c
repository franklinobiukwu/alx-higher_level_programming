#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - create odd numbered list palindrome and check if it is a palindrome
 *
 * Return: Always 0.
 */
int main(void)
{
	listint_t *head;

	head = NULL;
	add_nodeint_end(&head, 98);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 727);
	add_nodeint_end(&head, 972);
	add_nodeint_end(&head, 727);
	add_nodeint_end(&head, 0);
	add_nodeint_end(&head, 50);
	add_nodeint_end(&head, 98);
	print_listint(head);

	if (is_palindrome(&head) == 1)
		printf("Linked list is a palindrome\n");
	else
		printf("Linked list is not a palindrome\n");

	free_listint(head);
	return (0);
}	
