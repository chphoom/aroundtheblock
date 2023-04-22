import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map, filter, from, last, throwError } from 'rxjs';
import { Post } from './models';
export { Post } from './models';

@Injectable({
  providedIn: 'root'
})
export class PostsService {

  constructor(private http: HttpClient) {}

  /**
   * Retrieve all Posts in the system.
   * 
   * @returns an observable array of Post objects.
   */
  getAllPosts(): Observable<Post[]> {
    return this.http.get<Post[]>("/api/posts");
  }

  /**
   * Retrieve Post from id.
   * 
   * @returns an observable Post object.
   */
  getPost(id: Number): Observable<Post> {
    return this.http.get<Post>(`/api/posts/${id}`);
  }

  /**
   * Create a Post.
   * 
   * @returns a new Post.
   */
  createPost(post: Post): Observable<Post> {
    /* const post: Post = {
      id:9,
      img:"lucy.png",
      desc:"testing",
      private:true,
      created:null,
      postedBy:"elaine13@email.unc.edu",
      challenge:1,
      comments:[],
      tags:[]
    } */
    console.log("reached service with image file: " + post.img)
    return this.http.post<Post>("/api/createpost", post);
  }

  /**
   * Delete a Post.
   * 
   * @returns the deleted Post.
   */
  deletePost(post: Post, options: Array<String>): Observable<Post> {
    return this.http.delete<Post>("/api/delete/posts/"+post.id);
  }

  /**
   * Retrieve all meChallenge Posts in the system.
   * 
   * @returns an observable array of Post objects.
   */
  getMePosts(): Observable<Post[]> {
    return this.http.get<Post[]>("/api/meposts");
  }

  /**
   * Retrieve all weChallenge Posts in the system.
   * 
   * @returns an observable array of Post objects.
   */
  getWePosts(): Observable<Post[]> {
    return this.http.get<Post[]>("/api/weposts");
  }
}
