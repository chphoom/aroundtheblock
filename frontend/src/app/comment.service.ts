import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, map, filter, from, last, throwError } from 'rxjs';
import { Comment, User } from './models';
export { Comment } from './models';

@Injectable({
  providedIn: 'root'
})
export class CommentService {

  constructor(private http: HttpClient) {}

  createComment(_text: string, user: User, post_id: number) {
    let newcomment: Comment = {id:undefined, commenter:user.email, post:post_id, replies:[], text:_text, created:new Date()}
    return this.http.post<Comment>("/api/comment", newcomment)
  }
}
