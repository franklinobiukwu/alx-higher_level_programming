#include "lists.h"


/**
 * add_dnodeint - Function that adds node at the
 * beginning of a dlistint_t list
 *
 * @head: ponter to head of list
 * @n: value of node
 *
 * Return: Address of new element or NULL if fail
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new_node;
	dlistint_t temp;

	/*Create new Node*/
	new_node = malloc(sizeof(dlistint_t));

	/*Return NULL if malloc fail*/
	if (new_node == NULL)
		return (NULL);
	/*Initialize Node*/
	new_node->n = n;
	new_node->prev = NULL;
	new_node->next = NULL;

	/*Add node*/
	if (*head == NULL)
		*head = new_node;
	else
	{
		if ((*head)->prev == NULL)
		{
			temp.next = *head;
			*head = new_node;
			new_node->next = temp.next;
		}
		else
			*head = (*head)->prev;
	}

	return (new_node);
}
