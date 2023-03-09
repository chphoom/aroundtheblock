import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError, map } from 'rxjs';

export interface User {
  email: string;
  displayName: string;
  password: string;
  created: Date;
  private: boolean;
  bio: string;
  pronouns: string;
  img: string;
}

/**
 * This class handles the registration concerns of the system including the ability
 * to create new registrations and retrieve a list of registered users.
 */
@Injectable({
  providedIn: 'root'
})
export class RegistrationService {

  constructor(private http: HttpClient) {}

  /**
   * Retrieve all users registered with the check-in system.
   * 
   * @returns observable array of User objects.
   */
  getUsers(): Observable<User[]> {
    return this.http.get<User[]>("/api/registrations").pipe(map(users=>users.map(user => {
      user.created = new Date(user.created);
      return user;
    })));
  }

  /**
   * Registers a user with the check-in system.
   * 
   * @param email 
   * @param displayName username
   * @param password
   * @param created
   * @returns Obervable of User that will error if there are issues with validation or persistence.
   */
  registerUser(email: string, displayName: string, password: string): Observable<User> {
    let errors: string[] = [];

    //TODO: email  validation
    if (email === "") {
      errors.push(`Email required.`);
    }
    // if (pid.toString().length !== 9) {
    //   errors.push(`Invalid PID: ${pid}`);
    // }

    if (displayName === "") {
      errors.push(`Username required.`);
    }

    if (password === "") {
      errors.push(`Password required.`)
    }

    if (errors.length > 0) {
      return throwError(() => { return new Error(errors.join("\n")) });
    }

    let user: User = {email, displayName, password, created: new Date(), private: true, bio: "", pronouns: "", img: ""};

    return this.http.post<User>("api/registrations",user);
  }

}
