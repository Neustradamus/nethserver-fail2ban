Summary: NethServer configuration for fail2ban
Name: nethserver-fail2ban
Version: 1.0.7
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name}
BuildRequires: nethserver-devtools
Requires: fail2ban fail2ban-shorewall perl-Email-Valid
#AutoReq: no

%description
NethServer configuration for fail2ban

%prep
%setup

%pre
#With NS7 < RC4 firewalld was not disabled
#with the stable version, it could be removed
/usr/bin/systemctl stop firewalld >/dev/null 2>&1
/usr/bin/systemctl disable firewalld >/dev/null 2>&1

%post
%preun

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

%{__mkdir_p} -p $RPM_BUILD_ROOT/var/run/fail2ban

%{genfilelist} %{buildroot} \
  --file /usr/libexec/nethserver/fail2ban-status 'attr(0755,root,root)' \
  --file /usr/bin/fail2ban-listban 'attr(0750,root,root)' \
  --file /usr/bin/fail2ban-unban 'attr(0750,root,root)' \
  --file /usr/libexec/nethserver/fail2ban-listban 'attr(0755,root,root)' \
  --file /usr/libexec/nethserver/fail2ban-listip 'attr(0755,root,root)' \
  --file /usr/libexec/nethserver/shorewall-nethserver 'attr(0750,root,root)' \
$RPM_BUILD_ROOT > e-smith-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Fri Sep 28 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.7-1
- Wrong error path for the roundcubemail log - Bug NethServer/dev#5592

* Tue Sep 25 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.6-1
- Fail2Ban: asterisk notification always enabled - Bug NethServer/dev#5586

* Mon Aug 13 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.5-1
- Fail2ban: Status section to display statistics - NethServer/dev#5546
- Asterisk jail for fail2ban - NethServer/dev#5543
- Fail2ban triggers backup-config run every night - NethServer/dev#5565

* Fri Jun 08 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.4-1
- Fail2ban: do not start a jail when the log is missing - Bug NethServer/dev#5518

* Sun May 27 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.3-1
- Blank Dashboard after updates - Bug NethServer/dev#5508
- Code from dnutan

* Fri May 25 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.2-1
- Fail2ban dies if ban/unban is impossible. 
- IP Key suppression and unban if ban counter is > 2

* Tue May 15 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.1-1
- Remove the define settings in spec file

* Tue May 15 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-1
- Fail2Ban: collect statistics of permanent jail ban - NethServer/dev#5480
- Fail2Ban: dovecot brute force attack not recognized - Bug NethServer/dev#5481
- Fail2ban: Documentation and Travis code - NethServer/dev#5489

* Sat Apr 07 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.37-1.ns7
- recidive jail delete the esmith key

* Wed Feb 28 2018  Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.36-1.ns7
- fail2ban database to fix the recidive unban issue
- fix typo for whitelisting and email address

* Mon Feb 26 2018  Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.35-1.ns7
- Back to shorewall

* Sun Feb 25 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.34-1.ns7
- Recidive jail can be perpetual

* Sun Feb 25 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.32-1.ns7
- Use iptables for banAction instead of shorewall

* Thu Feb 15 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.31-1.ns7
- relax nethserver-dovecot about 'Disconnected (auth failed'

* Sat Jan 20 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.30-1.ns7
- nethserver-dovecot jail less restrictive for 'Disconnected' regex

* Fri Dec 08 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.29-1.ns7
- Button creation to restart fail2ban in the gui

* Sat Nov 11 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.28-1.ns7
- Validate the content of IgnoreIP & CustomDestemail in nethgui

* Sun Nov 05 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.27-1.ns7
- template of /etc/logrotate.d/fail2ban

* Thu Nov 02 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.26-1.ns7
- Revert the wildcard 0.1.25-1.ns7
- restart fail2ban on trusted network expand

* Thu Oct 19 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.25-1.ns7
- Restart fail2ban service on trusted-network
- back to the * wildcard
- reload the fail2ban configuration when logrotate

* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.24-1.ns7
- Restart httpd service on trusted-network

* Sat Aug 19 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.23-1.ns7
- escape path file for sogo jail , code from phonon112358

* Fri Jul 28 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.22-1.ns7
- Start sogo jail if the log exists

* Tue Jul 18 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.21-1.ns7
- Fix variable error on owncloud jail

* Sat Jul 15 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.20-1.ns7
- Custom MaxRetry property per jail (only by db)
- Remove MaxRetry recidive listed twice

* Thu Jun 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.18-1.ns7
- Add translation description

* Thu Jun 22 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.17-1.ns7
- Removed the wildcard on watched log files

* Thu Jun 22 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.16-1.ns7
- Test if the fail2ban log exists for recidive jail

* Mon Jun 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.15-1.ns7
- Stop to send notifications on start/stop jails
- UI tweaks
- Code from dnutan <dnutan@openaliasbox.org>

* Fri Jun 09 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.14-1.ns7
- Test if the dovecot log exists before to start the dovecot/sieve jails

* Wed May 03 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.13-1-ns7
- postfix-ddos jail updated

* Tue May 02 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.12-1-ns7
- Added postfix-ddos jail
- Added dovecot-nethserver Jail
- Added pam-generic-nethserver jail

* Mon May 01 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.11-1-ns7
- adjusted log file and backend in jail

* Mon May 01 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.10-1-ns7
- Added custom regex against dovecot and pam-generic
- pam-generic.local & dovecot.local

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.9-1-ns7
- Template expansion on trusted-network

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.8-2-ns7
- Added OPENVPN Jail
- Enforce the MaxRetry setting

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.7-2-ns7
- GPL license

* Mon Feb 27 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.7-1-ns7
- added phpmyadmin jail

* Mon Feb 27 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.6-1-ns7
- added wildcard in httpd log

* Fri Feb 24 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.5-1-ns7
- Corrected the email recipient

* Mon Feb 20 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.4-1-ns7
- Handle the log rotation by wildcard
- Create /var/run/fail2ban

* Tue Jan 31 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.3-2-ns7
- Firewalld is stopped and disabled in %pre

* Wed Nov 23 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.3-1-ns7
- urbackup jail is templated now

* Mon Nov 21 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.2-1-ns7
- Urbackup Jail created

* Sun Nov 6 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.1-1-ns7
- Nextcloud jail created

* Sun Nov 6 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.1.0-1-ns7
- NS7 adaptation

* Tue Mar 8 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.7-ns6
- Owncloud Jail created

* Tue Mar 8 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.7-ns6
- Owncloud Jail created

* Sat Mar 5 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.6-ns6
- Fail2ban panel uses Tab now
- Blacklist tab created with Unban Input Box

* Sat Feb 20 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.5-ns6
- New jail against bad authentication to httpd-admin
- Help page created
- Enhancement of the jail status  with expandable menu.

* Thu Jan 28 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.4-ns6
- WebUI enhanced

* Wed Jan 27 2016 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.3-ns6
- WebUI designed

* Wed Dec 02 2015 Stephane de Labrusse <stephdl@de-labrusse.fr> - 0.0.2-ns6
- Initial release
