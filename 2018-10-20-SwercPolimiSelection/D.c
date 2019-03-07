
// A C / C++ program for Prim's Minimum  
// Spanning Tree (MST) algorithm. The program is  
// for adjacency matrix representation of the graph 
#include <stdio.h> 
#include <limits.h> 
#include<stdbool.h> 
#include<math.h>
// Number of vertices in the graph 
int V; 
  
// A utility function to find the vertex with  
// minimum key value, from the set of vertices  
// not yet included in MST 
double minKey(double key[], bool mstSet[]) 
{ 
// Initialize min value 
    int min = INT_MAX, min_index; 
      
    for (int v = 0; v < V; v++) 
        if (mstSet[v] == false && key[v] < min) 
            min = key[v], min_index = v; 
      
    return min_index; 
} 
  
// A utility function to print the  
// constructed MST stored in parent[] 
void printMax(int parent[], int n, double graph[V][V]) 
{ 
    int max = 0;
    for (int i = 1; i < V; i++) 
        if(max < ceil(graph[i][parent[i]]))
            max = ceil(graph[i][parent[i]]);

    printf("%d", max);
} 
  
// Function to construct and print MST for  
// a graph represented using adjacency  
// matrix representation 
void primMST(double graph[V][V]) 
{ 
    // Array to store constructed MST 
    int parent[V];  
    // Key values used to pick minimum weight edge in cut 
    double key[V];  
    // To represent set of vertices not yet included in MST 
    bool mstSet[V];  
  
    // Initialize all keys as INFINITE 
    for (int i = 0; i < V; i++) 
        key[i] = INT_MAX, mstSet[i] = false; 
  
    // Always include first 1st vertex in MST. 
    // Make key 0 so that this vertex is picked as first vertex. 
    key[0] = 0;      
    parent[0] = -1; // First node is always root of MST  
  
    // The MST will have V vertices 
    for (int count = 0; count < V-1; count++) 
    { 
        // Pick the minimum key vertex from the  
        // set of vertices not yet included in MST 
        int u = minKey(key, mstSet); 
  
        // Add the picked vertex to the MST Set 
        mstSet[u] = true; 
  
        // Update key value and parent index of  
        // the adjacent vertices of the picked vertex.  
        // Consider only those vertices which are not  
        // yet included in MST 
        for (int v = 0; v < V; v++) 
  
        // graph[u][v] is non zero only for adjacent vertices of m 
        // mstSet[v] is false for vertices not yet included in MST 
        // Update the key only if graph[u][v] is smaller than key[v] 
        if (graph[u][v] && mstSet[v] == false && graph[u][v] < key[v]) 
            parent[v] = u, key[v] = graph[u][v]; 
    } 
  
    // print the constructed MST 
    printMax(parent, V, graph); 
} 
  
  
// driver program to test above function 
int main() 
{ 
    scanf("%d", &V);

    double graph[V][V];
    int xy[V][2];

    for(int i=0; i<V; i++) {
        scanf("%d", &xy[i][0]);
        scanf("%d", &xy[i][1]);

        graph[i][i] = 0;
        for(int j=i-1; j>=0; j--) {
            graph[i][j] = sqrt((double)( pow((xy[i][0]-xy[j][0]), 2) + pow((xy[i][1]-xy[j][1]), 2)) );
            graph[j][i] = graph[i][j];
        }
    }
  
    // Print the solution 
    primMST(graph); 
  
    return 0; 
} 