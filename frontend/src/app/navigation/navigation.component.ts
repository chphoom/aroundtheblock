import { Component, ElementRef, ViewChild } from '@angular/core';
import { RegistrationService } from '../registration.service';
import { User } from '../registration.service';
import { Router } from '@angular/router';
import { NotificationService, Notification } from '../notification.service';
import { PostsService } from '../posts.service';
import { CommentService, Comment } from '../comment.service';
import { Observable, map, of, shareReplay } from 'rxjs';
import { ChallengeService, Challenge } from '../challenge.service';

@Component({
  selector: 'app-navigation',
  templateUrl: './navigation.component.html',
  styleUrls: ['./navigation.component.css']
})
export class NavigationComponent {
  public notifs!: Notification[]
  numUnread!: number;
  public user: User | undefined;
  // public countdownMap: Map<number, string> = new Map<number, string>();
  @ViewChild('search', { static: true }) search!: ElementRef;

  constructor(private router: Router,
     public registration_service: RegistrationService,
     public notificationService: NotificationService,
     private commentService: CommentService,
     private challengeService: ChallengeService) {
    this.registration_service.getUserInfo().subscribe((user: User) => {
      this.user = user;
      this.notificationService.getToUser(user.email).subscribe(
        (_Ns: Notification[]) => {
          this.notifs = _Ns;
          of(this.notifs.filter(n => !n.read).length).subscribe(
            (num: number) => {
              this.numUnread = num;
            }
          )
        }
      )
    });
  }

  onSearch() {
    const query = this.search.nativeElement.value;
    // For example, you could navigate to the search page and pass the search term as a query parameter
    this.router.navigate(['/search', query]);  }

    onClickN(notif: Notification) {
      if (notif.comment_id) {
        this.notificationService.read(notif.id!).subscribe(
          (update: Notification) => {
            this.commentService.get(update.comment_id!).subscribe(
              (comment: Comment) => {
                this.router.navigate(['/post', comment.post]).then(() => {
                  // The navigation has completed, so you can safely perform any post-navigation actions here
                });
              }
            )
          }
        )
      } else if (notif.challenge_id) {
        this.notificationService.read(notif.id!).subscribe(
          (update: Notification) => {
            this.router.navigate(['/we-challenge']);
          }
        )
      } else {
        // handle some error idk
      }
    }
    
  private userCache: { [key: string]: Observable<string> } = {};

  getUsername(notif: Notification): Observable<string> {
    const cachedValue = this.userCache[notif.fromUser_id!];
    if (cachedValue) {
      return cachedValue;
    }
    const newValue = this.registration_service.getUser(notif.fromUser_id!).pipe(
      map(user => user ? `${user.displayName}` : ''),
      shareReplay(1) // cache the result
    );
    this.userCache[notif.fromUser_id!] = newValue;
    return newValue;
  }

  logOut() {
    this.registration_service.logout();
    this.router.navigate(['/']);
  }

  private challengeCache: { [key: string]: Observable<string> } = {};

  challengeString(notif: Notification): Observable<string> {
    const cachedValue = this.challengeCache[notif.challenge_id!];
    if (cachedValue) {
      return cachedValue;
    }

    const newValue = new Observable<string>((observer) => {
      this.challengeService.getChallenge(notif.challenge_id!).subscribe(
        (challenge: Challenge) => {
          // Calculate the current date and challenge end date
          const currentDate = new Date();
          const challengeEndDate = new Date(challenge.end!);

          // Calculate the difference in milliseconds between the two dates
          const timeDiff = challengeEndDate.getTime() - currentDate.getTime();

          // Convert the difference to days
          const oneDayInMs = 24 * 60 * 60 * 1000;
          const daysDiff = timeDiff / oneDayInMs;

          // Check if the difference is less than or equal to 1 day
          if (daysDiff <= 1) {
            // The current date is within one day of challenge.end
            // Add your logic here
            this.notificationService.unread(notif.id!).subscribe(() => {});
            observer.next('Current challenge ends soon!');
          } else {
            // The current date is more than one day away from challenge.end
            // Add your logic here
            observer.next(`Current challenge ends on ${challengeEndDate.toLocaleDateString(undefined, { month: 'short', day: 'numeric', year: 'numeric' })}`);
          }
          observer.complete();
        },
        (error) => {
          observer.error(error);
        }
      );
    });

    this.challengeCache[notif.challenge_id!] = newValue;
    return newValue;
  }
}
