#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);
bool ciclo(int len, int v[], int pos);
void imprimir_matriz();

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++) // para cada votante
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i]) == 0) // tengo que actualizar
        {
            ranks[rank] = i; // ranks[rank]: índice del candidato en posición rank.
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < candidate_count - 1; i++) // i representa el rank ganador
    {
        for (int j = i + 1; j < candidate_count; j++) // j representa a los que pierden contra i
        {
            preferences[ranks[i]][ranks[j]] += 1;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (int i = 0; i < candidate_count - 1; i++)
    {
        for (int j = i + 1; j < candidate_count; j++)
        {
            if (preferences[i][j] > preferences[j][i])
            {
                pairs[pair_count].winner = i;
                pairs[pair_count].loser = j;
                pair_count++;
            }
            if (preferences[i][j] < preferences[j][i])
            {
                pairs[pair_count].winner = j;
                pairs[pair_count].loser = i;
                pair_count++;
            }
        }
    }

    return;
}

// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    // Hallamos un vector que determine la fuerza de cada par
    int strenght[pair_count], aux_int;
    pair aux_pair;
    for (int i = 0; i < pair_count; i++)
    {
        strenght[i] = preferences[pairs[i].winner][pairs[i].loser];
    }

    for (int i = 0; i < pair_count; i++) // cantidad de veces
    {
        for (int j = 0; j < pair_count - 1; j++)
        {
            if (strenght[j + 1] > strenght[j])
            {
                aux_int = strenght[j + 1];
                strenght[j + 1] = strenght[j];
                strenght[j] = aux_int;

                aux_pair = pairs[j + 1];
                pairs[j + 1] = pairs[j];
                pairs[j] = aux_pair;
            }
        }
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (int i = 0; i < pair_count; i++)
    {
        // Añado el par a la tabla locked
        locked[pairs[i].winner][pairs[i].loser] = true;

        // Hay un ciclo ahora?

        for (int j = 0; j < candidate_count; j++) // esto va a definir el inicio. Cada candidato va a ser el origen
        {
            int vec[pair_count + 1];
            vec[0] = j;

            if (ciclo(pair_count + 1, vec, 0)) // si hay un ciclo ([limiteDeElementos], vector, posicion)
            {
                // Volver al estado inicial
                locked[pairs[i].winner][pairs[i].loser] = false;
            }
        }
    }

    return;
}

// Print the winner of the election
void print_winner(void)
{
    // imprimir_matriz();

    for (int j = 0; j < candidate_count; j++)
    {
        bool winner = true;
        for (int i = 0; i < candidate_count; i++)
        {
            if (locked[i][j])
            {
                winner = false;
            }
        }
        if (winner)
        {
            printf("%s\n", candidates[j]);
            return;
        }
    }

    return;
}

bool ciclo(int len, int v_orig[], int pos) // prueba el recibido y a cada uno de los que pueda llegar
{
    // int v_new[len]

    // Primero, probamos si es que en el vector recibido no hay bucles
    for (int i = 0; i < pos; i++)
    {
        for (int j = i + 1; j <= pos; j++)
        {
            if (v_orig[i] == v_orig[j])
            {
                return true;
            }
        }
    }

    for (int i = 0; i < candidate_count; i++)
    {
        if (i != v_orig[pos]) // v_orig[pos]: candidato
        {
            if (locked[v_orig[pos]][i] && pos + 1 < len)
            {
                v_orig[pos + 1] = i;
                if (ciclo(len, v_orig, pos + 1))
                {
                    return true;
                }
            }
        }
    }

    return false;
}

void imprimir_matriz()
{
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            printf("%d ", locked[i][j]);
        }
        printf("\n");
    }
}
