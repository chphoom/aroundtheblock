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

  getAll() {
    return this.http.get<Comment>("/api/comments")
  }

  get(id: number) {
    return this.http.get<Comment>("/api/getcomment/"+id)
  }

  createComment(_text: string, user: User, post_id: number) {
    let newcomment: Comment = {id:undefined, commenter:user.email, user_id:user.email, post:post_id, replyTo_id:null, replies:[], text:_text, created:new Date()}
    
    return this.http.post<Comment>("/api/comment", newcomment)
  }

  deleteComment(comment: Comment){
    return this.http.delete<Comment>("api/delete/comment/"+comment.id)
  }

  editComment(comment_id: number, newText: string){
    return this.http.put<Comment>(`api/comment/edit?comment_id=${comment_id}&newText=${newText}`,{})
  }

  createReply(comment_id: number, _text: string, user: User){
    let newcomment: Comment = {id:undefined, commenter:user.email, user_id:user.email, post:0, replyTo_id:comment_id, replies:[], text:_text, created:new Date()}
    return this.http.post<Comment>(`api/reply?comment_id=${comment_id}`, newcomment)
  }
}
