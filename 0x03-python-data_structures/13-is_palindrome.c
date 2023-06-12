#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *strt, *rev, *mid;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	strt = *head;
	while (strt)
	{
		size++;
		strt = strt->next;
	}

	strt = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		strt = strt->next;

	if ((size % 2) == 0 && strt->n != strt->next->n)
		return (0);

	strt = strt->next->next;
	rev = reverse_listint(&strt);
	mid = rev;

	strt = *head;
	while (rev)
	{
		if (strt->n != rev->n)
			return (0);
		strt = strt->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
