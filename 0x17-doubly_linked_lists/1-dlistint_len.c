#include "lists.h"
#include <stddef.h>


/**
 * dlistint_len - returns the number of node
 * in a dlistint_t list
 *
 * @h: list head
 *
 * Return: Number of nodes in list
 */

size_t dlistint_len(const dlistint_t *h)
{
	size_t count = 0;

	if (h == NULL)
		return (count);
	/*Count nodes in List*/
	while (h)
	{
		count++;
		h = h->next;
	}

	return (count);
}
