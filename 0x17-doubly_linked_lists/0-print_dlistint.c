#include "lists.h"
#include <stddef.h>

/**
 * print_dlistint - Function that prints all
 * the elements of a dlistint_t list
 *
 * @h : pointer to list
 *
 * Return: number of node in list
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	/*Return -1 if list is NULL*/
	if (h == NULL)
		return (0);
	/*Print List*/
	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}

	return (count);
}
