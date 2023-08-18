#include "lists.h"
#include <stddef.h>

/**
 * add_dnodeint_end - Function that adds node
 * at the end of a dlistint_t list
 *
 * @head: pointer to list head
 * @n: value of new node
 *
 * Retuen: Address of new node or NULL if fail
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new_node;
	dlistint_t *mover;
	dlistint_t temp;

	mover = *head;
	/*Create new node*/
	new_node = malloc(sizeof(dlistint_t));

	/*Return NULL if malloc fails*/
	if (new_node == NULL)
		return (NULL);
	/*Initialize new node*/
	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = NULL;

	/*Add node to end of list*/
	if (*head == NULL)
		*head = new_node;
	else
	{
		/*Traverse List*/
		while (mover)
		{
			temp.next = mover;
			mover = mover->next;
		}
		temp.next->next = new_node;
	}

	return (new_node);
}
