import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError, map } from 'rxjs';

export interface User {
  pid: number;
  first_name: string;
  last_name: string;
}

@Injectable({
  providedIn: 'root'
})
export class DeleteService {

  constructor(private http: HttpClient) { }

  deleteUser(user: User): Observable<User> {
    //let newUser: User = {user.pid, };
    return this.http.delete<User>("api/delete/"+user.pid);
  }
}
