#include "lists.h"

/**
 * insert_node- inserts a number into a sorted singly linked list
 * @head: head of the linked list
 * @number: number to insert
 * Return:the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->data = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->data)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		listint_t *current = *head;

		while (current->next != NULL && current->next->data < number)
		{
			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
