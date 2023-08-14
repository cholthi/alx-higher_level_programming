#include <stdlib.h>
#include "lists.h"


/** is_palindrome - Checks if linked list iis a palindrome
 * @head: Head of a singly linked list
 *
 * Return: int 1 if palindrome or 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half, *prev_of_slow = *head;
	listint_t *mid = NULL;
	int res = 1;


	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
			{
				fast = fast->next->next;
				prev_of_slow = slow;
				slow = slow->next;
			}
		if (fast != NULL)
		{
			mid = slow;
			slow = slow->next;
		}

		second_half = slow;
		prev_of_slow->next = NULL;
		reverse(&second_half);
		res = compare_list(*head, second_half);
		reverse(&second_half);

		if (mid != NULL)
		{
			prev_of_slow->next = mid;
			mid->next = second_half;
		} else
			prev_of_slow->next  = second_half;
	}


	return (res);

}

/** reverse - Reverses a singly linked list
 * @head: Head pointer of the singly linked list
 *
 * Return: lisint_t new pointer to the head
 */
void reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		current = next;
	}

	*head = prev;
}

/** compare_list - Compare two singly linked list nodes
 * @node_a: first listint_t node to compare
 * @node_b: second listint_t to compare
 *
 * Return: int bool
 */
int compare_list(listint_t *node_a, listint_t *node_b)
{
	listint_t *temp_a = node_a;
	listint_t *temp_b = node_b;

	while (temp_a && temp_b)
	{
		if (temp_a->n == temp_b->n)
		{
			temp_a = temp_a->next;
			temp_b = temp_b->next;
		} else
		{
			return 0;
		}
	}

	if (temp_a == NULL && temp_b == NULL)
		return 1;

	return 0;
}
