#include "lists.h"

/**
  * check_cycle - checks if a cycle.
  * @list: arg
  *
  * Return: 1 or 0
  */
int check_cycle(listint_t *list)
{
	listint_t *curr, *next_n;

	if (list == NULL)
		return (0);

	curr = list;
	next_n = list;

	while (curr && next_n && next_n->next)
	{
		curr = curr->next;
		next_n = next_n->next->next;
		if (curr == next_n)
			return (1);
	}
	if (curr != next_n)
		return (0);
	return (1);
}
