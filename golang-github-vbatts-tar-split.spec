# Run tests in check section
%bcond_without check

# https://github.com/vbatts/tar-split
%global goipath         github.com/vbatts/tar-split
Version:                0.11.1

%global common_description %{expand:
Pristinely disassembling a tar archive, and stashing needed raw bytes and
offsets to reassemble a validating original archive.}

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Tar archive assembly/dis-assembly
# Detected licences
# - BSD 3-clause "New" or "Revised" License at 'LICENSE'
License:        BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/Sirupsen/logrus)
BuildRequires: golang(github.com/urfave/cli)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%build
%gobuildroot
%gobuild -o _bin/tar-split %{goipath}/cmd/tar-split


%install
%goinstall
install -Dpm 0755 _bin/tar-split %{buildroot}%{_bindir}/tar-split


%if %{with check}
%check
%gochecks
%endif


%files
%license LICENSE
%doc README.md
%{_bindir}/tar-split


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Nov 23 2018 Steve Baker <sbaker@redhat.com> - 0.11.1-1
- rebuilt for upstream 0.11.1

* Fri Nov 23 2018 Steve Baker <sbaker@redhat.com> - 0.11.0-1
- rebuilt for upstream 0.11.0
- update to new Go packaging

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-3
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.13-2
- https://fedoraproject.org/wiki/Changes/golang1.6

* Tue Feb 16 2016 Antonio Murdaca <runcom@fedoraproject.org> - 0.9.13-1
- rebuilt for upstream 0.9.13

* Thu Jan 28 2016 Antonio Murdaca <runcom@redhat.com> - 0.9.12-1
- First package for Fedora
