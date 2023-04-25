import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map, filter, from, last, throwError } from 'rxjs';
import { Post, Challenge, User } from './models';
export { Post, Challenge, User } from './models';

@Injectable({
  providedIn: 'root'
})
export class SearchService {

  constructor(private http: HttpClient) {}

  Posts(query: string): Observable<Post[]>{
    return this.http.get<Post[]>(`/api/searchposts/${query}`);
  }

  Tagged(query: string): Observable<Post[]>{
    return this.http.get<Post[]>(`/api/tagged/${query}`);
  }

  Challenges(query: string): Observable<Challenge[]>{
    return this.http.get<Challenge[]>(`/api/searchchallenges/${query}`);
  } 

  Users(query: string): Observable<User[]>{
    return this.http.get<User[]>(`/api/searchusers/${query}`);
  }
}
