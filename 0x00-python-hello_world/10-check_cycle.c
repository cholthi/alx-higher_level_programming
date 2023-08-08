#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Detects loops in a singly linked list
 * @list: Head of the loop
 * Return: 1 if loop present or 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;

		if (fast == slow)
			return (0);
	}

	return (1);
}
