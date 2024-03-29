import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError, map } from 'rxjs';
import { Challenge, User } from './models';
export { User } from './models';

@Injectable({
  providedIn: 'root'
})
export class DeleteService {

  constructor(private http: HttpClient) { }

  deleteUser(user: User): Observable<User> {
    //let newUser: User = {user.pid, };
    return this.http.delete<User>("api/delete/users/"+user.email);
  }

  deleteChallenge(challenge: Challenge): Observable<Challenge> {
    return this.http.delete<Challenge>("api/delete/challenges/"+challenge.id)
  }
}
