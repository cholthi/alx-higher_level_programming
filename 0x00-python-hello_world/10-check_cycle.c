#include "lists.h"


/**
 * check_cycle - Detechs loops in a singly linked list
 * @list: listint_t A pointer to a head node of linked list
 * Desc: Uses Floyd’s Cycle-Finding Algorithm
 *
 * Return: int 0 if no loops or 1 if loops detected
 */
int check_cycle(listint_t *list)
{
	listint_t *slow=list,*fast=NULL;
    
	if(!list || !(list->next))
		return (0);

	fast=list->next;

	while(slow!=fast)
	{
		if(fast==NULL)
		{
			return (0);
		}
		slow=slow->next;
		if(fast->next && fast->next->next)
			fast=fast->next->next;
		else
			fast = fast->next;
	}
	return (1);
}
