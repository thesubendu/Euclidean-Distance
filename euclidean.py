import matplotlib.pyplot as plt
import numpy as np

def euclidean_distance(p1, p2):
    """Calculate Euclidean distance between two points."""
    return np.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def get_coordinates():
    """Get coordinates from user input."""
    print("Enter coordinates for Point 1:")
    x1 = float(input("  x1: "))
    y1 = float(input("  y1: "))
    
    print("\nEnter coordinates for Point 2:")
    x2 = float(input("  x2: "))
    y2 = float(input("  y2: "))
    
    return (x1, y1), (x2, y2)

def plot_points(p1, p2, distance):
    """Create a graph showing the two points and the distance between them."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Plot the points
    ax.plot(p1[0], p1[1], 'ro', markersize=10, label=f'Point 1 ({p1[0]}, {p1[1]})')
    ax.plot(p2[0], p2[1], 'bo', markersize=10, label=f'Point 2 ({p2[0]}, {p2[1]})')
    
    # Draw a line between the points
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'g--', linewidth=2, 
            label=f'Distance = {distance:.2f}')
    
    # Add labels to the points
    ax.annotate(f'P1\n({p1[0]}, {p1[1]})', xy=p1, xytext=(10, 10), 
                textcoords='offset points', fontsize=10, color='red')
    ax.annotate(f'P2\n({p2[0]}, {p2[1]})', xy=p2, xytext=(10, 10), 
                textcoords='offset points', fontsize=10, color='blue')
    
    # Set labels and title
    ax.set_xlabel('X-axis', fontsize=12)
    ax.set_ylabel('Y-axis', fontsize=12)
    ax.set_title('Euclidean Distance Visualization', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='best')
    ax.axis('equal')
    
    plt.tight_layout()
    plt.show()

def main():
    print("=" * 50)
    print("EUCLIDEAN DISTANCE CALCULATOR")
    print("=" * 50)
    
    # Get coordinates from user
    point1, point2 = get_coordinates()
    
    # Calculate Euclidean distance
    dist = euclidean_distance(point1, point2)
    
    # Display result
    print("\n" + "=" * 50)
    print(f"Euclidean Distance: {dist:.4f}")
    print("=" * 50)
    
    # Plot the graph
    plot_points(point1, point2, dist)

if __name__ == "__main__":
    main()
