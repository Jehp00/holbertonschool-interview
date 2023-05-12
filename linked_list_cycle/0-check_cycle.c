#include "lists.h"


/**
 * check_cycle - checks if a single linked list has a cycle inside
 * @list: A pointer to the head of the list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    if (list == NULL || list->next == NULL)
        return (0);

    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        slow = slow->next;

        if (slow == fast)
            return (1);
    }
    return (0);
}
