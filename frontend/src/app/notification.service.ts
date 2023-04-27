import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, map, filter, from, last, throwError } from 'rxjs';
import { Notification } from './models';
export { Notification } from './models';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {

  constructor(private http: HttpClient) {}

  /**
   * Retrieve all Notifs in the system.
   * 
   * @returns an observable array of Notif objects.
   */
  all(): Observable<Notification[]> {
    return this.http.get<Notification[]>("/api/notifs");
  }

   /**
   * Retrieve Notif from id.
   * 
   * @returns an observable Notif object.
   */
  get(id: Number): Observable<Notification> {
    return this.http.get<Notification>(`/api/notifs/id/${id}`);
  }

  /**
   * Create a Notif.
   * 
   * @returns a new Notif.
   */
  new(notif: Notification): Observable<Notification> {
    return this.http.post<Notification>("/api/notifs/new", notif);
  }

  /**
   * Delete a Notif.
   * 
   * @returns the deleted Notif.
   */
  delete(id: number): Observable<Notification> {
    return this.http.delete<Notification>("/api/delete/notif/"+id);
  }

  /**
   * Retrieve Notif from toUser
   * 
   * @returns an observable Notif object.
   */
  getToUser(email: string): Observable<Notification[]> {
    return this.http.get<Notification[]>(`/api/notifs/to/${email}`);
  }

   /**
   * Retrieve Notif from fromUser
   * 
   * @returns an observable Notif object.
   */
  getFromUser(email: string): Observable<Notification[]> {
    return this.http.get<Notification[]>(`/api/notifs/from/${email}`);
  }

  /**
   * Read a Notifcation.
   * 
   * @returns a Notification.
   */
  read(id: number): Observable<Notification> {
    return this.http.put<Notification>(`/api/notifs/read/${id}`,{});
  }

  /**
   * Unread a Notifcation.
   * 
   * @returns a Notification.
   */
  unread(id: number): Observable<Notification> {
    return this.http.put<Notification>(`/api/notifs/unread/${id}`,{});
  }


}//end of class
