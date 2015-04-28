package edu.nnu.gu;

import java.util.Random;

import com.github.davidmoten.rtree.Entry;
import com.github.davidmoten.rtree.RTree;
import com.github.davidmoten.rtree.geometry.Point;

import static com.github.davidmoten.rtree.geometry.Geometries.*;


public class TestRtree {
	
	public static void main(String[] args) {
		
		//random 100 points x_i in [0, 1000) and y_i in [0, 1000)
		double [] X = randomIntArray(100, 0, 1000, 20150428L);
		double [] Y = randomIntArray(100, 0, 1000, 20150428L);
		
		double qx = 500.0f;
		double qy = 500.0f;
		double maxDist= 50.0f;
		
		System.out.println("Brute-force query without using R-Tree : ");
		query_without_rtree(X, Y, qx, qy, maxDist);

		
		System.out.println("==========================================================================================================================================================================");
		RTree<String, Point> tree = buildRTree(X, Y);
		System.out.println("First construct R-Tree : visualization is saved in target/R-Tree.png");
		tree.visualize(500, 500).save("target/R-Tree.png");
		System.out.println("Then query using R-Tree : ");
		query_using_rtree(tree, qx, qy, maxDist);

	}
	
	
	public static double[] randomIntArray(int n, int min, int max, long seed){
		double arr[] = new double[n];
		Random rand = new Random(seed);
		for (int i = 0; i < arr.length; i++) {
			arr[i] = rand.nextInt((max - min) + 1) + min;
		}
		return arr;
	}
	
	public static double distance(double x1, double y1, double x2, double y2){
		return Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)); 
	}
	
	public static void query_without_rtree(double[] X, double[] Y, double qx, double qy, double maxDist){
		for (int i = 0; i < X.length; i++) {
			double dist = distance(X[i],Y[i], qx, qy);
			if( dist < maxDist){
				System.out.println(String.format("Found (%f,%f), distance to (%f,%f) is %f", X[i], Y[i], qx, qy, dist));
			}
		}
	}
	
	public static RTree<String, Point> buildRTree(double[] X, double[] Y){
		RTree<String, Point> tree = RTree.create();
		for (int i = 0; i < X.length; i++) {
			tree = tree.add(""+i, point(X[i], Y[i]));
		}
		return tree;
	}
	
	public static void query_using_rtree(RTree<String, Point> tree, double qx, double qy, double maxDist){
		Iterable<Entry<String, Point>> results = tree.search(point(qx, qy), maxDist).toBlocking().toIterable();
		for (Entry<String, Point> result : results) {
			Point p = result.geometry();
			double dist = distance(p.x(), p.y(), qx, qy);
			System.out.println(String.format("Found (%f,%f), distance to (%f,%f) is %f", p.x(), p.y(), qx, qy, dist));
		}
	}
}
