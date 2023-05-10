#include "lists.h"


/**
 * check_cycle - Detechs loops in a singly linked list
 * @list: listint_t A pointer to a head node of linked list
 * Desc: Uses Floyd’s Cycle-Finding Algorithm
 *
 * Return: int 0 if no loops or 1 if loops detected
 */
int check_cycle(listint_t *h)
{
	listint_t *slow=h,*fast=NULL;
    
	if(!h || !(h->next))
		return false;

	fast=h->next;

	while(slow!=fast)
	{
		if(fast==NULL)
		{
			return false;
		}
		slow=slow->next;
		if(fast->next && fast->next->next)
			fast=fast->next->next;
		else
			fast = fast->next;
	}
	return true;
}
