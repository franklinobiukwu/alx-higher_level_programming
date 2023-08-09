#include "lists.h"

/**
* insert_node - function that inserts a numberinto a sorted singly linked list
*
* @head: head of singly linked list
* @number: number to be added to the sorted linked list
*
* Return: address of new node, or NULL on failure
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	/* store number in new node */
	new_node->n = number;
	new_node->next = NULL;
	/* set head to point to new node if head is null */
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	/*
	 * check through the sorted list for number is less than
	 * the next node, but greater than or equal to previous node
	 */
	current = *head;
	prev = *head;
	while (current)
	{
		if (current->n < number)
		{
			prev = current;
			current = current->next;
		}
		else
		{
			if (prev == head)
				head = new_node;
			else
				prev->next = new_node;
			new_node->next = current;
			break;
		}
	}
	/*
	 * insert new node at the end of the list
	 * if traversed to the end of the list
	 */
	if (current == NULL)
		prev->next = new_node;
	return (new_node);
}
