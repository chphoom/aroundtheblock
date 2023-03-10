import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError, map } from 'rxjs';
import { User } from './models';
export { User } from './models';

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
  registerUser(email: string, displayName: string, password: string, confirm: string): Observable<User> {
    let errors: string[] = [];

    //TODO: email  validation
    if (email === "") {
      errors.push(`Email required.`);
    }

    if (displayName === "") {
      errors.push(`Username required.`);
    }

    if (password === "") {
      errors.push(`Password required.`)
    }
    
    if (password !== confirm) {
      errors.push('Please confirm that your passwords match')
    }

    if (errors.length > 0) {
      return throwError(() => { return new Error(errors.join("\n")) });
    }

    let user: User = {email, displayName, password, created: new Date(), private: true, bio: "", pronouns: "", img: "", userPosts: [], savedChallenges: [], savedPosts: [], connectedAccounts: []};

    return this.http.post<User>("api/registrations",user);
  }

  loginUser(email: string, password: string){
    const body = new URLSearchParams();
    body.set('username', email);
    body.set('password', password);

    return this.http.post('/api/login', body.toString(), {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    });
  }

}
