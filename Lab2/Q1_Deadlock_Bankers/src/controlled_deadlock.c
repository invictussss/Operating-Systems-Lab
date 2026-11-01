#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include <errno.h>
#include <unistd.h>

pthread_mutex_t resourceA = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_t resourceB = PTHREAD_MUTEX_INITIALIZER;

pthread_barrier_t barrier;

void *deadlock_demo(void *arg)
{
    int id = *(int *)arg;

    if (id == 1)
    {
        pthread_mutex_lock(&resourceA);
        printf("Thread 1: Holding Resource A\n");
    }
    else
    {
        pthread_mutex_lock(&resourceB);
        printf("Thread 2: Holding Resource B\n");
    }

    pthread_barrier_wait(&barrier);

    printf("Thread %d: Waiting for second resource\n", id);

    struct timespec timeout;
    clock_gettime(CLOCK_REALTIME, &timeout);
    timeout.tv_sec += 2;

    int result;

    if (id == 1)
        result = pthread_mutex_timedlock(&resourceB, &timeout);
    else
        result = pthread_mutex_timedlock(&resourceA, &timeout);

    if (result == 0)
    {
        printf("Thread %d: Acquired second resource\n", id);

        if (id == 1)
            pthread_mutex_unlock(&resourceB);
        else
            pthread_mutex_unlock(&resourceA);
    }
    else if (result == ETIMEDOUT)
    {
        printf("Thread %d: Timeout! Releasing held resource.\n", id);
    }

    if (id == 1)
        pthread_mutex_unlock(&resourceA);
    else
        pthread_mutex_unlock(&resourceB);

    return NULL;
}

void *ordered_demo(void *arg)
{
    int id = *(int *)arg;

    printf("Thread %d: Following resource order A -> B\n", id);

    pthread_mutex_lock(&resourceA);
    pthread_mutex_lock(&resourceB);

    printf("Thread %d: Both resources acquired safely\n", id);

    pthread_mutex_unlock(&resourceB);
    pthread_mutex_unlock(&resourceA);

    return NULL;
}

int main()
{
    pthread_t t1, t2;
    int id1 = 1, id2 = 2;

    printf("\n--- Controlled Deadlock Scenario ---\n");

    pthread_barrier_init(&barrier, NULL, 2);

    pthread_create(&t1, NULL, deadlock_demo, &id1);
    pthread_create(&t2, NULL, deadlock_demo, &id2);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    pthread_barrier_destroy(&barrier);

    printf("\n--- Deadlock Prevention: Resource Ordering ---\n");

    pthread_create(&t1, NULL, ordered_demo, &id1);
    pthread_create(&t2, NULL, ordered_demo, &id2);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    printf("\nProgram completed successfully.\n");

    pthread_mutex_destroy(&resourceA);
    pthread_mutex_destroy(&resourceB);

    return 0;
}
